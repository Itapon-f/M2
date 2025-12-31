/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_find.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: agiron-d <agiron-d@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/27 16:36:48 by agiron-d          #+#    #+#             */
/*   Updated: 2025/11/27 17:39:03 by agiron-d         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	ft_assign_index_2(t_stack **stack, int nbr, int size)
{
	t_stack	*compare;
	int		index;
	int		j;

	compare = *stack;
	index = 0;
	j = 0;
	while (j < size)
	{
		if (compare->nbr < nbr)
			index++;
		compare = compare->next;
		j++;
	}
	return (index);
}

void	ft_assign_index(t_stack **stack)
{
	t_stack	*current;
	int		size;
	int		i;

	if (!stack || !*stack)
		return ;
	size = ft_stack_size(*stack);
	current = *stack;
	i = 0;
	while (i < size)
	{
		current->i = ft_assign_index_2(stack, current->nbr, size);
		current = current->next;
		i++;
	}
}

int	ft_find_position_of_min(t_stack *stack)
{
	long	min;
	t_stack	*current;
	int		pos;
	int		min_pos;

	if (!stack)
		return (0);
	min = ft_find_min(stack);
	current = stack;
	pos = 0;
	min_pos = 0;
	while (pos < ft_stack_size(stack))
	{
		if (current->nbr == min)
		{
			min_pos = pos;
			break ;
		}
		current = current->next;
		pos++;
	}
	return (min_pos);
}
