/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_stack_do_moves.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: agiron-d <agiron-d@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/27 12:48:21 by agiron-d          #+#    #+#             */
/*   Updated: 2025/11/28 08:14:28 by agiron-d         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_rotate_to_min(t_stack **stack)
{
	int	min_pos;
	int	size;

	if (!stack || !*stack)
		return ;
	min_pos = ft_find_position_of_min(*stack);
	size = ft_stack_size(*stack);
	if (min_pos <= size / 2)
	{
		while (min_pos-- > 0)
			ft_ra(stack, 1);
	}
	else
	{
		while (min_pos++ < size)
			ft_rra(stack, 1);
	}
}

void	ft_ra_rrab(t_stack **from, t_stack **to,
	t_count_moves *moves, int to_size)
{
	int	to_down;

	to_down = to_size - moves->to_up;
	while (moves->from_up > 0)
	{
		ft_rb(from, 1);
		moves->from_up--;
	}
	while (to_down > 0)
	{
		ft_rra(to, 1);
		to_down--;
	}
}

void	ft_rra_rb(t_stack **from, t_stack **to,
	t_count_moves *moves, int from_size)
{
	int	from_down;

	from_down = from_size - moves->from_up;
	while (from_down > 0)
	{
		ft_rrb(from, 1);
		from_down--;
	}
	while (moves->to_up > 0)
	{
		ft_ra(to, 1);
		moves->to_up--;
	}
}
