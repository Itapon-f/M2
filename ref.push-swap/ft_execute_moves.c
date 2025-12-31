/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_execute_moves.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: agiron-d <agiron-d@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/27 13:37:19 by agiron-d          #+#    #+#             */
/*   Updated: 2025/12/02 15:36:36 by agiron-d         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	ft_is_sorted(t_stack *stack)
{
	t_stack	*current;
	int		size;
	int		i;

	if (!stack)
		return (1);
	size = ft_stack_size(stack);
	if (size <= 1)
		return (1);
	current = stack;
	i = 0;
	while (i < size - 1)
	{
		if (current->nbr > current->next->nbr)
			return (0);
		current = current->next;
		i++;
	}
	return (1);
}

static void	ft_execute_moves_to_b(t_stack **a, t_stack **b)
{
	int	size;
	int	pushed;

	size = ft_stack_size(*a);
	pushed = 0;
	while (size > 3 && pushed < size - 3)
	{
		ft_pb(a, b, 1);
		pushed++;
	}
}

static void	ft_execute_moves_to_a(t_stack **a, t_stack **b)
{
	t_count_moves	*current_moves;
	int				b_size;

	while (*b)
	{
		b_size = ft_stack_size(*b);
		current_moves = ft_calc_moves(b, a, b_size);
		if (current_moves)
		{
			ft_execute_calculated_moves(b, a, current_moves);
			ft_pa(a, b, 1);
			free(current_moves);
		}
		else
		{
			ft_pa(a, b, 1);
		}
	}
}

void	ft_execute_moves_start(t_stack **a, t_stack **b)
{
	int	size;

	if (!a || !*a)
		return ;
	ft_assign_index(a);
	size = ft_stack_size(*a);
	if (ft_is_sorted(*a))
		return ;
	if (size <= 3)
	{
		ft_sort_small(a, b);
		return ;
	}
	ft_execute_moves_to_b(a, b);
	if (ft_stack_size(*a) == 3)
		ft_sort_three(a);
	ft_execute_moves_to_a(a, b);
	ft_rotate_to_min(a);
}
